import {useEffect, useState} from 'react';
import {fetchRaceResult, RaceResultType} from '@/models/raceResult';
import {fetchRaceInfo, RaceInfoType} from '@/models/raceInfo';
import RaceResult from "@/components/templates/raceResult";


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
        <RaceResult
            raceResults={apiRaceResults}
            raceInfo={apiRaceInfo}
        />
    );
}

export default ResultIndex;