export async function fetchRaceInfo() {
    const response = await fetch('http://localhost:8080/api/result/raceinfo/');
    const data: RaceInfoResponse[] = await response.json();

    if (data.length === 0) {
        return null;
    }

    const obj = data[0];
    const date = new Date(obj.race_date);
    return {
        id: obj.id,
        raceId: obj.race_id,
        raceDate: date,
        venue: obj.get_venue_display,
        raceClass: obj.race_class,
        raceNumber: obj.race_number,
        trackType: obj.get_track_type_display,
        trackCondition: obj.get_track_condition_display,
        direction: obj.get_direction_display,
        distance: obj.distance,
        weather: obj.get_weather_display,
    }
}

type RaceInfoResponse = {
    id: number;
    race_id: number;
    race_date: string;
    get_venue_display: string;
    race_class: number;
    race_number: number;
    get_track_type_display: number;
    get_track_condition_display: number;
    get_direction_display: number;
    distance: number;
    get_weather_display: number;
}

export type RaceInfoType = {
    id: number;
    raceId: number;
    raceDate: Date;
    venue: string;
    raceClass: number;
    raceNumber: number;
    trackType: number;
    trackCondition: number;
    direction: number;
    distance: number;
    weather: number;
}