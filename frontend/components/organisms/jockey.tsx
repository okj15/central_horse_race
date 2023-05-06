import {JockeyResultType} from "@/pages/api/jockey";
import Table from "react-bootstrap/Table";

function JockeyResult(props: { jockeyResults: JockeyResultType[] }) {
    return (
        <div>
            <Table striped bordered hover>
                <thead>
                <tr>
                    <th scope="col">騎手名</th>
                    <th scope="col">1位</th>
                    <th scope="col">2位</th>
                    <th scope="col">3位</th>
                    <th scope="col">4位以下</th>
                </tr>
                </thead>
                <tbody>
                {props.jockeyResults.map((item: JockeyResultType) => (
                    <tr key={item.id}>
                        <td>{item.name}</td>
                        <td>{item.first}</td>
                        <td>{item.second}</td>
                        <td>{item.third}</td>
                        <td>{item.unplaced}</td>
                    </tr>
                ))}
                </tbody>
            </Table>
        </div>
    );
}

export default JockeyResult;