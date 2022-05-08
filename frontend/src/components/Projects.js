import React from "react";


const ProjectItem = ({project,deleteProject}) =>{

    return(
    <tr>
        <td>
            {project.name}
        </td>
        <td>
            {project.users}
        </td>
        <td>
            <button onClick={()=>deleteProject(project.id)} type="button">
                Удалить
            </button>
        </td>
    </tr>

    )
}

const ProjectList = ({projects,deleteProject})=>{
    return(
    <table>
        <th>
            Project name
        </th>
        <th>
            Users list
        </th>

        {projects.map((project)=><ProjectItem project={project} deleteProject={deleteProject}/>)}
        <tr>
            <button type="button">
                Создать
            </button>
        </tr>
    </table>
    )
}

export default ProjectList;