import {useEffect, useState} from "react";
import {fetchHorseResult, HorseResultType} from "@/models/horseResult";
import {useRouter} from "next/router";

function HorseResultDetail() {
    const [apiHorseResults, setApiHorseResults] = useState<HorseResultType>();

    const router = useRouter();
    const {horseId} = router.query;

    useEffect(() => {
        if (!router.isReady) return;

        async function getData() {
            const horseResult: HorseResultType | undefined = await fetchHorseResult(horseId as string);
            setApiHorseResults(horseResult);
        }

        getData().then(r => console.log(r));
    }, [horseId, router]);

    return (
        <div>HorseResultDetail{apiHorseResults?.name}</div>
    )

}

export default HorseResultDetail;