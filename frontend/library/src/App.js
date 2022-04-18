import logo from './logo.svg';
import './App.css';
import axios from 'axios'


//componentDidMount() {
//   axios.get('http://127.0.0.1:8000/api/users')
//       .then(response => {
//           const users = response.data
//               this.setState(
//               {
//                   'users': users
//               }
//           )
//       }).catch(error => console.log(error))
//}






function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
