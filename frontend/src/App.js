import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import './App.css';
import { add, remove, set} from './reducers/todosReducer'
import * as api from "./api/todo"


function App() {
  return (
    <div className="App">
      <h1>App</h1>
    </div>
  );
}

export default App;
