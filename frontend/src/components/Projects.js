import React from "react";


const ProjectItem = ({project}) =>{

    return(
    <tr>
        <td>
            {project.name}
        </td>
        <td>
            {project.users}
        </td>
        <td>
            <button type="button">
                Удалить
            </button>
        </td>
    </tr>

    )
}

const ProjectList = ({projects})=>{
    return(
    <table>
        <th>
            Project name
        </th>
        <th>
            Users list
        </th>

        {projects.map((project)=><ProjectItem project={project}/>)}
        <tr>
            <button type="button">
                Создать
            </button>
        </tr>
    </table>
    )
}

export default ProjectList;