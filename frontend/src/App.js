import React from 'react';
import './App.css';
import Classifier from './components/Classifier/Classifier';
import ImageLIst from './components/ImageList/ImageList';
import Navigation from './components/Navigation/Navigation';
import { Link } from 'react-router-dom';
import {Route, BrowserRouter, Switch} from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Navigation />
      <div className='App'>
        <Switch>
          <Route exact path='/' component={Classifier} />
          <Route exact path='/list' component={ImageLIst} />
          <Route exact path='*' component={Classifier} />
        </Switch>
      </div>
    </BrowserRouter>
  );
}

export default App;


// import React from 'react';
// import './App.css';
// import Classifier from './components/Classifier/Classifier';
// import ImageLIst from './components/ImageList/ImageList';
// import Navigation from './components/Navigation/Navigation';
// import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";


// function App() {
//   return (
//     <BrowserRouter>
//       <Navigation />
//       <div className='App'>
//       <Routes>
//         <Route path="/" element={<Classifier/>} />
//         <Route path="/list" element={<ImageLIst/>} />
//         <Route path="*" element={<Classifier/>} />
//       </Routes>


//         {/* <Switch>
//           <Route exact path='/' component={Classifier} />
//           <Route exact path='/list' component={ImageLIst} />
//           <Route exact path='*' component={Classifier} />
//         </Switch> */}
//       </div>
//     </BrowserRouter>
//   );
// }

// export default App;