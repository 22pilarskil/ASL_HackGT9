import Letter from "../../../frontend/src/components/Letter";
import HandSign from "../../../frontend/src/components/HandSign";
import PractCol1 from "../../../frontend/src/components/PractCol1";

function Prompts() {
    return (
    <div id="Allprompts">
        <div id="letterDisplay">
        <Letter data={""}></Letter>
        </div>
        <div id="handDisplay">
        <HandSign data={""}></HandSign>
        </div>
    </div>
    );
}

export default Prompts;