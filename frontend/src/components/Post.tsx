import React from "react";

interface postData {
    title: string,
    body: string,
    id: string,
    votes: number
}

const Post = (props: postData) => {
    return (
        <div>
            <h3 className="text-2xl font-semibold truncate">{props.title}</h3>
            <br />
            <p className="text-xl truncate">{props.body}</p>
            <br />
            <p className="text-lg">Votes: {props.votes}</p>
        </div>
    );
}

export default Post;