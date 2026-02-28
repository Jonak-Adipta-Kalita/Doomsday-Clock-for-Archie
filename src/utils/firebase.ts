import { initializeApp, getApps, getApp } from "firebase/app";
import { getFirestore, setDoc, getDoc, doc, collection } from "firebase/firestore";

export type Data = {
	message: string;
	user: string | null;
	time: number;
	timestamp: string,
}

const firebaseConfig = {
	apiKey: "AIzaSyCMNouWMvMVFt_L-JUa6D4WETqXeZTnJGA",
	authDomain: "senior-citizen-doomsday-clock.firebaseapp.com",
	projectId: "senior-citizen-doomsday-clock",
	storageBucket: "senior-citizen-doomsday-clock.firebasestorage.app",
	messagingSenderId: "855910342990",
	appId: "1:855910342990:web:776c592d08b85a45687e1f"
};

const app = !getApps().length ? initializeApp(firebaseConfig) : getApp();

export const db = getFirestore(app);

const messagesRef = collection(db, "Messages");
const latestMessageRef = doc(messagesRef, "latest");

export const getTime = async () => {
	const latestMessage = await getDoc(latestMessageRef);

	if (latestMessage.exists()) return latestMessage.data()

	const newData: Data = {
		message: "",
		user: null,
		time: 1,
		timestamp: new Date().toISOString()
	}

	await setDoc(latestMessageRef, newData);

	return newData;
};

export const changeTime = async (data: Data) => {
	const latestMessage = (await getDoc(latestMessageRef)).data();

	await setDoc(doc(messagesRef, latestMessage.timestamp), latestMessage);

	await setDoc(latestMessageRef, data);
};

export const loginUser = async (name: string, password: string) => {
	const userRef = doc(db, "Users", name);

	try {
		const userData = (await getDoc(userRef)).data();

		if (userData.password === password) return true;
	} catch (err) {
		return false;
	}

	return false;
};
