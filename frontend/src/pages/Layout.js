import { Outlet, Link } from "react-router-dom";

const Layout = () => {
  return (
    <>
      <div class="navStyle">
            <Link class="link" to="Home">Home</Link>
            <Link class="link" to="Practice">Practice</Link>
            <Link class="link" to="Translate">Translate</Link>
      </div>

      <Outlet />
    </>
  )
};

export default Layout;