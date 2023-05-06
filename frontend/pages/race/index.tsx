import {useEffect, useState} from 'react';
import {fetchRaceResult, RaceResultType} from '@/pages/api/raceResult';
import {fetchRaceInfo, RaceInfoType} from '@/pages/api/raceInfo';
import {fetchJockeyResult, JockeyResultType} from "@/pages/api/jockey";
import Race from "@/components/templates/race";


function RaceIndex() {
    const [apiRaceInfo, setApiRaceInfo] = useState<RaceInfoType | null>(null);
    const [apiRaceResults, setApiRaceResults] = useState<RaceResultType[]>([]);
    const [apiJockeyResults, setApiJockeyResults] = useState<JockeyResultType[]>([]);

    useEffect(() => {
        async function getData() {
            const raceInfo: RaceInfoType | null = await fetchRaceInfo();
            setApiRaceInfo(raceInfo);

            const raceResults: RaceResultType[] = await fetchRaceResult();
            setApiRaceResults(raceResults);

            const jockeyResults: JockeyResultType[] = await fetchJockeyResult();
            setApiJockeyResults(jockeyResults);
        }

        getData().then(r => console.log(r));
    }, []);

    return (
        <Race
            raceResults={apiRaceResults}
            raceInfo={apiRaceInfo}
            jockeyResults={apiJockeyResults}
        />
    );
}

export default RaceIndex;