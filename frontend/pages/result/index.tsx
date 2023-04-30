import {useEffect, useState} from 'react';
import {fetchRaceResult, RaceResultType} from '@/models/raceResult';
import {fetchRaceInfo, RaceInfoType} from '@/models/raceInfo';
import Table from 'react-bootstrap/Table';
import RaceInfo from "@/components/organisms/raceInfo";


function ResultIndex() {
    const [apiRaceInfo, setApiRaceInfo] = useState<RaceInfoType | null>(null);
    const [apiRaceResults, setApiRaceResults] = useState<RaceResultType[]>([]);

    useEffect(() => {
        async function getData() {
            const raceInfo: RaceInfoType | null = await fetchRaceInfo();
            setApiRaceInfo(raceInfo);

            const raceResults: RaceResultType[] = await fetchRaceResult();
            setApiRaceResults(raceResults);
        }

        getData().then(r => console.log(r));
    }, []);

    return (
        <div>
            <RaceInfo raceInfo={apiRaceInfo} />
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
                {apiRaceResults.map((item: RaceResultType) => (
                    <tr key={item.id}>
                        <td>{item.rank}</td>
                        <td>{item.bracket}</td>
                        <td>{item.horseNumber}</td>
                        <td>{item.horseName}</td>
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
        </div>
    );
}

export default ResultIndex;