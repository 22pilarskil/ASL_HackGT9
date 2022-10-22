import { Outlet, Link } from "react-router-dom";

const Layout = () => {
  return (
    <>
      <div className="navStyle">
            <Link className="link" to="Home">Home</Link>
            <Link className="link" to="Practice">Practice</Link>
            <Link className="link" to="Translate">Translate</Link>
      </div>

      <Outlet />
    </>
  )
};

export default Layout;