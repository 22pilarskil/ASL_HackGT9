import React from "react";
import { Nav, NavLink, NavMenu } 
    from "/Nav";

function Navigation() {
    return (
        <Nav>
            <NavMenu><ul>
                <li>
                    <NavLink to="/">HOME</NavLink>
                </li>
                <li>
                    <NavLink to="/Practice">HOME</NavLink>
                </li>
                <li>
                    <NavLink to="/Translate">HOME</NavLink>
                </li>
            </ul></NavMenu>
        </Nav>

    );
}

export default Navigation;