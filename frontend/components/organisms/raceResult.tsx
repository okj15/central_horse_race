import {RaceResultType} from "@/pages/api/raceResult";
import Table from 'react-bootstrap/Table';
import Link from 'next/link';


function RaceResult(props: { raceResults: RaceResultType[] }) {
    return (
        <Table striped bordered hover>
            <thead>
            <tr>
                <th>着順</th>
                <th>枠</th>
                <th>馬番</th>
                <th>馬名</th>
                <th>性別</th>
                <th>年齢</th>
                <th>斤量</th>
                <th>レースタイム</th>
                <th>人気</th>
                <th>オッズ</th>
                <th>騎手</th>
                <th>馬主</th>
                <th>調教師</th>
            </tr>
            </thead>
            <tbody>
            {props.raceResults.map((item: RaceResultType) => (
                <tr key={item.id}>
                    <td>{item.rank}</td>
                    <td>{item.bracket}</td>
                    <td>{item.horseNumber}</td>
                    <td>
                        <Link
                            href={`/result/horse/${encodeURIComponent(item.horseId)}`}>{item.horseName}</Link>
                    </td>
                    <td>{item.gender}</td>
                    <td>{item.age}</td>
                    <td>{item.jockeyWeight}</td>
                    <td>{item.raceTime}</td>
                    <td>{item.popularity}</td>
                    <td>{item.odds}</td>
                    <td>{item.jokeyName}</td>
                    <td>{item.ownerName}</td>
                    <td>{item.trainerName}</td>
                </tr>
            ))}
            </tbody>
        </Table>
    )
}

export default RaceResult;

