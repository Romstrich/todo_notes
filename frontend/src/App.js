import React from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import UserList from "./components/Users.js"
import ProjectList from "./components/Projects.js"
import TodoList from "./components/Todo_notes.js"

class App extends React.Component{
    constructor(props){
        super(props);
        this.state={
            'users':[],
            'projects':[],
            'todo_notes':[]
        }
    }

    componentDidMount(){

        axios.get("http://127.0.0.1:8000/api/users/").then(response=>{
        this.setState(
            {'users':response.data}
        )}).catch(error => console.log(error))

        axios.get("http://127.0.0.1:8000/api/projects/").then(response=>{
        this.setState(
            {'projects':response.data}
        )}).catch(error => console.log(error))

        axios.get("http://127.0.0.1:8000/api/todo_notes/").then(response=>{
        this.setState(
            {'todo_notes':response.data}
        )}).catch(error => console.log(error))
    }

    render(){
    return (
            <div>
                <TodoList todo_notes={this.state.todo_notes}/>
            </div>
        );
    return (
            <div>
                <ProjectList projects={this.state.projects}/>
            </div>
        );
//        return (
//            <div>
//                <UserList users={this.state.users}/>
//            </div>
//        );

    }
}

export default App;
