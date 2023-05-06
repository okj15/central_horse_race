export async function fetchJockeyResult(raceId: number = 202101010101) {
    const url = `http://localhost:8080/api/jockey/results/?race=${raceId}`;
    const response = await fetch(url);
    const data: JockeyResultResponse[] = await response.json();

    const jockeyResults: JockeyResultType[] = [];
    for (const obj of data) {
        jockeyResults.push({
            id: obj.id,
            year: obj.year,
            rank: obj.rank,
            first: obj.first,
            second: obj.second,
            third: obj.third,
            unplaced: obj.unplaced,
            gradedRuns: obj.graded_runs,
            gradedWins: obj.graded_wins,
            specialRuns: obj.special_runs,
            specialWins: obj.special_wins,
            generalRuns: obj.general_runs,
            generalWins: obj.general_wins,
            turfRuns: obj.turf_runs,
            turfWins: obj.turf_wins,
            dirtRuns: obj.dirt_runs,
            dirtWins: obj.dirt_wins,
            winRate: obj.win_rate,
            quinellaRate: obj.quinella_rate,
            showRate: obj.show_rate,
            earnings: obj.earnings,
            name: obj.jockey.name
        });
    }

    return jockeyResults;
}


type JockeyMasterResponse = {
    id: number;
    name: string;
}

type JockeyResultResponse = {
    id: number;
    year: number;
    rank: number;
    first: number;
    second: number;
    third: number;
    unplaced: number;
    graded_runs: number;
    graded_wins: number;
    special_runs: number;
    special_wins: number;
    general_runs: number;
    general_wins: number;
    turf_runs: number;
    turf_wins: number;
    dirt_runs: number;
    dirt_wins: number;
    win_rate: number;
    quinella_rate: number;
    show_rate: number;
    earnings: number;
    jockey: JockeyMasterResponse;
}

export type JockeyResultType = {
    id: number;
    year: number;
    rank: number;
    first: number;
    second: number;
    third: number;
    unplaced: number;
    gradedRuns: number;
    gradedWins: number;
    specialRuns: number;
    specialWins: number;
    generalRuns: number;
    generalWins: number;
    turfRuns: number;
    turfWins: number;
    dirtRuns: number;
    dirtWins: number;
    winRate: number;
    quinellaRate: number;
    showRate: number;
    earnings: number;
    name: string;
}