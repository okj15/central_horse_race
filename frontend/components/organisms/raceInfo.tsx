import {RaceInfoType} from "@/pages/api/raceInfo";

function RaceInfo(props: { raceInfo: RaceInfoType | null }) {
    return (
        <div>
            <p>開催日: {props.raceInfo?.raceDate.toLocaleDateString()}</p>
            <p>開催場所: {props.raceInfo?.venue}</p>
            <p>{props.raceInfo?.trackType}{props.raceInfo?.direction}{props.raceInfo?.distance}</p>
            <p>{props.raceInfo?.weather}</p>
            <p>{props.raceInfo?.trackType}:{props.raceInfo?.trackCondition}</p>
        </div>
    )
}

export default RaceInfo;