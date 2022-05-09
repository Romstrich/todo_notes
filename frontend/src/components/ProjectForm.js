import React from "react";





class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {name: '', users: ''}
    }

    handleChange(event){
        this.setState(
        {
            [event.target.name]: event.target.value
        }
        );
        console.log(event.target.name,event.target.value)
    }

    handleSubmit(event) {
        console.log(this.state.name,this.state.users)
        event.preventDefault()
    }




    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
            <div className="form-group">

            <label htmlFor="login">name</label>

            <input type="text" name="name" placeholder="name"
            value={this.state.name} onChange={(event)=>this.handleChange(event)} />

            </div>

            <div className="form-group">
            <label htmlFor="users">users</label>

            <input type="nomber" name="users" placeholder="users"
            value={this.state.users} onChange={(event)=>this.handleChange(event)} />
            <input type="submit" value="SAVE" />
            </div>
            </form>
        );
    }
}
export default ProjectForm;