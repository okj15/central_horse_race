import {useEffect, useState} from 'react';
import {fetchApiData, RaceResult} from '@/models/result';
import Table from 'react-bootstrap/Table';
import RaceInfo from "@/components/organisms/raceInfo";


function ResultIndex() {
    const [apiRaceResult, setApiRaceResult] = useState<RaceResult | null>(null);
    const [apiRaceResults, setApiRaceResults] = useState<RaceResult[]>([]);

    useEffect(() => {
        async function getData() {
            const data: RaceResult[] = await fetchApiData();
            setApiRaceResults(data);
            if (data.length > 0) {
                setApiRaceResult(data[0]);
            }
        }

        getData().then(r => console.log(r));
    }, []);

    return (
        <div>
            <RaceInfo raceResult={apiRaceResult} />
            <Table striped bordered hover>
                <thead>
                <tr>
                    <th>枠</th>
                    <th>馬番</th>
                    <th>馬名</th>
                    <th>性別</th>
                    <th>年齢</th>
                    <th>斤量</th>
                    <th>レースタイム</th>
                    <th>人気</th>
                    <th>オッズ</th>
                    {/*<th>騎手</th>*/}
                    {/*<th>馬主</th>*/}
                    {/*<th>調教師</th>*/}
                    {/*<th>生産者</th>*/}
                </tr>
                </thead>
                <tbody>
                {apiRaceResults.map((item: RaceResult) => (
                    <tr key={item.id}>
                        <td>{item.bracket}</td>
                        <td>{item.horseNumber}</td>
                        <td>{item.horse}</td>
                        <td>{item.getGenderDisplay}</td>
                        <td>{item.age}</td>
                        <td>{item.jockeyWeight}</td>
                        <td>{item.raceTime}</td>
                        <td>{item.popularity}</td>
                        <td>{item.odds}</td>
                    </tr>
                ))}
                </tbody>
            </Table>
        </div>
    );
}

export default ResultIndex;