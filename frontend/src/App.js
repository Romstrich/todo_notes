import React from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import UserList from "./components/Users.js";
import ProjectList from "./components/Projects.js";
import TodoList from "./components/Todo_notes.js";
import LoginForm from "./components/Auth.js";
import ProjectForm from "./components/ProjectForm.js";
import {HashRouter, Route, BrowserRouter,Link, Switch,Redirect} from "react-router-dom";
import Cookies from "universal-cookie";
//import { Link } from 'react-router';



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

    createProject(name,users){
        const headers=this.get_headers()
        const data={name:name,users:[users]}
        axios.post(`http://127.0.0.1:8000/api/projects/`,data,{headers}).then(response=>{
        this.load_data()
        }).catch(error => console.log(error))
        alert(`http://127.0.0.1:8000/api/projects/`)
    console.log(name,users)
    }

    deleteProject(id){
        const headers=this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/projects/${id}/`,{headers}).then(response=>{
        this.load_data()
        }).catch(error => console.log(error))
        alert(`http://127.0.0.1:8000/api/projects/${id}/`)
        console.log(id)
    }



    load_data(){
    const headers=this.get_headers()
    axios.get("http://127.0.0.1:8000/api/users/",{headers}).then(response=>{
        this.setState(
            {'users':response.data}
        )}).catch(error => console.log(error))

        axios.get("http://127.0.0.1:8000/api/projects/",{headers}).then(response=>{
        this.setState(
            {'projects':response.data}
        )}).catch(error => console.log(error))

        axios.get("http://127.0.0.1:8000/api/todo_notes/",{headers}).then(response=>{
        this.setState(
            {'todo_notes':response.data}
        )}).catch(error => console.log(error))
    }


    set_token(token){
//    console.log(token)
    const cookies=new Cookies()
    cookies.set('token',token)
    this.setState({'token':token},()=>this.load_data())
    }

    get_token(username,password){
        axios.post("http://127.0.0.1:8000/api-token-auth/",
        {'username':username,password:password})
        .then(response=>{this.set_token(response.data['token'])})
        .catch(error => console.log(error=>alert('Wrong login or password!!')))

    }

    is_auth(){
        return this.state.token
    }

    get_headers(){
        let headers={
        'Content-type':'applications/json'
        }
        if(this.is_auth()){
            headers['Authorization']=`Token ${this.state.token}`
            }
    }

    logout(){
        this.set_token('')
    }

    get_token_from_cookies(){
    const cookies=new Cookies()
    const token=cookies.get('token',token)
    this.setState({'token':token},()=>this.load_data())
    }



    componentDidMount(){
        //this.get_token_from_cookies()

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
                                <li>
                                    {this.is_auth() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                                </li>
                            </ul>
                       </nav>

            <Switch>
                    <Route exact path='/projects' component={()=> <ProjectList projects={this.state.projects} deleteProject={(id)=>this.deleteProject(id)}/>}/>

                    <Route exact path='/projects/create' component={()=> <ProjectForm
                    createProject={(name,users)=>this.createProject(name,users)}/>}/>

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
