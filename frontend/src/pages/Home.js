import handImage from "../assets/handimage.jpg";
function Home() {
    return (
        <div id="HomeComponent">
        <h1 className="main">Speak with your hands.</h1>
        <div id="home">
            <div id="T">
                <p style={{color:"black"}} className="right pHome">Explanation of project. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in.</p>
                <p style={{color:"black"}} className="right pHome">Explanation of project. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in.</p>
            </div>
            <div id="imgH">
                <img src={handImage} className="rotate homeimg"/>
            </div>
        </div>
        </div>
    );
}

export default Home;