import React from 'react';
import { Navbar, Nav } from 'react-bootstrap';

const Navigation = () => {
    return ( 
        <Navbar bg="dark" variant="dark" className="mb-3">
            <Navbar.Brand href="#home">Image Classifier</Navbar.Brand>
            <Nav className="mr-auto">
            <Nav.Link href="/">HOME</Nav.Link>
            <Nav.Link href="/list">RESULT LIST</Nav.Link>
            </Nav>
      </Navbar>
     );
}
 
export default Navigation;