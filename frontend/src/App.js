import React from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import UserList from "./components/Users.js"
import ProjectList from "./components/Projects.js"
import TodoList from "./components/Todo_notes.js"
import LoginForm from "./components/Auth.js"
import {HashRouter, Route, BrowserRouter,Link, Switch,Redirect} from "react-router-dom"



class App extends React.Component{
    constructor(props){
        super(props);
        this.state={
            'users':[],
            'projects':[],
            'todo_notes':[],
            'token':''
        }
    }

    set_token(token){
    }

    get_token(username,password){
        axios.post("http://127.0.0.1:8000/api-token-auth/",
        {'username':username,password:password})
        .then(response=>{this.set_token(response.data['token'])})
        .catch(error => console.log(error))

    }

    logout(){}


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

                <BrowserRouter>
                       <nav>
                            <ul>
                                <li>
                                    <Link to='/projects'> Projects </Link>
                                </li>
                                <li>
                                    <Link to='/todo_notes'> Todo notes </Link>
                                </li>
                                <li>
                                    <Link to='/users'> Users </Link>
                                </li>
                            </ul>
                       </nav>

            <Switch>
                    <Route exact path='/projects' component={()=> <ProjectList projects={this.state.projects}/>}/>
                    <Route exact path='/todo_notes' component={()=> <TodoList todo_notes={this.state.todo_notes}/>}/>
                    <Route exact path='/users' component={()=> <UserList users={this.state.users}/>}/>

                    <Route exact path='/login' component={()=> <LoginForm get_token={(username,password)=>this.get_token(username,password)}/>}/>


            </Switch>
                </BrowserRouter>
            </div>
        );
    }
}

export default App;
