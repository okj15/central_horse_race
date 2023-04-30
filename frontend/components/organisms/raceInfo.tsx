import {RaceInfoType} from "@/models/result";

function RaceInfo(props: {raceInfo: RaceInfoType | null}) {
    return (
        <div>
            <h1>RaceInfo</h1>
            <p>開催日: {props.raceInfo?.raceDate.toDateString()}</p>
            <p>開催場所: {props.raceInfo?.venue}</p>
            <p>{props.raceInfo?.trackType}{props.raceInfo?.direction}{props.raceInfo?.distance}</p>
            <p>{props.raceInfo?.weather}</p>
            <p>{props.raceInfo?.trackType}:{props.raceInfo?.trackCondition}</p>

        </div>
    )
}

export default RaceInfo