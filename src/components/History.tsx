import { useEffect, useState } from "react";
import { getHistory } from "../utils/firebase";
import moment from "moment";

const History = () => {
	const [data, setData] = useState<any | null>(null);

	useEffect(() => {
		const asyncFunc = async () => {
			const dbData = await getHistory();
			setData(dbData);
		}

		asyncFunc()
	}, [])

	if (data === null) return <p className="text-base text-gray-800/90 font-semibold">Loading Data...</p>;

	return (
		<div className="space-y-4">
			{data.map((message: any, i: number) => {
				const timestamp = moment(message.timestamp)

				return (
					<div key={i}>
						<p className="text-xl">
							<span className="font-bold text-orange-800">{message.user}</span>: {" "}
							<span className="font-semibold text-blue-800">&ldquo;{message.message}&rdquo;</span> {" "}
							<span className="font-bold text-teal-800 text-right">({message.time})</span>
						</p>
						<p className="text-base text-gray-800/90 font-semibold ml-5">on {timestamp.format("MMMM Do YYYY")} - {timestamp.fromNow()}</p>
					</div>
				)
			})}
		</div>
	)
}

export default History;
