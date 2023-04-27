import {useEffect, useState} from 'react';
import {fetchApiData} from '@/models/result';
import {RaceResult} from '@/models/result';


function ResultIndex() {
    const [apiData, setApiData] = useState<RaceResult[]>([]);

    useEffect(() => {
        async function getData() {
            const data: RaceResult[] = await fetchApiData();
            setApiData(data);
        }

        getData().then(r => console.log(r));
    }, []);

    // @ts-ignore
    return (
        <table>
            <thead>
            <tr>
                <th>馬番</th>
                <th>馬名</th>
                <th>性別</th>
                <th>年齢</th>
            </tr>
            {/*<th>斤量</th>*/}
            {/*<th>騎手</th>*/}
            {/*<th>タイム</th>*/}
            {/*<th>着差</th>*/}
            {/*<th>通過</th>*/}
            {/*<th>上り</th>*/}
            {/*<th>単勝</th>*/}
            {/*<th>人気</th>*/}
            {/*<th>馬体重</th>*/}
            {/*<th>調教師</th>*/}
            {/*<th>馬主</th>*/}
            {/*<th>賞金</th>*/}
            </thead>
            <tbody>
            {apiData.map((item: RaceResult) => (
                <tr key={item.id}>
                    <td>{item.horseNumber || 'a'}</td>
                    <td>{item.horse}</td>
                    <td>{item.getGenderDisplay}</td>
                    <td>{item.age}</td>
                </tr>
            ))}
            </tbody>
        </table>
    );
}

export default ResultIndex;