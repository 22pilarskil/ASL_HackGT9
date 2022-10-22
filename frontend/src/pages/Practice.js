import PractCol1 from "../components/PractCol1";
function Practice() {
    return (
        <div>
             <h1>PRACTICE</h1>
             <PractCol1 />
             <img src="{{ url_for('video_feed') }}" width="100%"/>

        </div>
       
    );
}

export default Practice;