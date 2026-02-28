import { useState } from "react"
import Clock from "./Clock";
import { loginUser } from "../utils/firebase";

const LoginUser = () => {
	const [username, setUsername] = useState<string>("");
	const [password, setPassword] = useState<string>("");

	const [user, setUser] = useState<string | null>(null);

	const tryLogin = async () => {
		const verifyCredentials = await loginUser(username, password)

		if (verifyCredentials) return setUser(username)

		alert("Wrong Credentials ;-;")
	};

	if (user === null) return (
		<div className="flex h-screen w-screen items-center justify-center">
			<div className="flex-col space-y-5 flex">
				<input className="input" placeholder="Name" value={username} onChange={(e) => setUsername(e.target.value!)} />
				<input className="input" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value!)} />
				<button className="button mt-10" onClick={() => tryLogin()}>Login</button>
			</div>
		</div>
	)

	return <Clock user={user} />
};

export default LoginUser;
