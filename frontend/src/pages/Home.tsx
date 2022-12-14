import React, { useCallback, useEffect, useState } from "react";
import Post from "../components/Post";
import axios from "axios";
import Header from "../components/Header";

interface PostData {
    title: string,
    body: string,
    id: string,
    votes: number,
    date: string
}

const Home = () => {

    const [posts, setPosts] = useState<PostData[] | any>();
    const [loading, setLoading] = useState(true);

    const [upvoteSend, setUpvoteSend] = useState(false);
    const [downvoteSend, setDownvoteSend] = useState(false);

    const [title, setTitle] = useState("");
    const [body, setBody] = useState("");

    const fetchUserData = async() => {
        const response = await axios.get("http://localhost:8000/posts");
        setPosts(response.data);
        setLoading(false);
    }

    const upvote = async(id: string) => {
        const url = "http://localhost:8000/posts/upvote";
        const params = {
            "id": id
        };
        const response = await axios.post(url, params);
        const currPosts = posts;

        console.log("Response Upvote: ", response);

        currPosts.forEach(
            (post: PostData) => {
                if (post.id === id) {
                    post.votes = response.data.votes;
                }
            }
        )        
        setPosts(currPosts);
    }

    const downvote = async(id: string) => {
        const url = "http://localhost:8000/posts/downvote";
        const params = {
            "id": id
        };
        const response = await axios.post(url, params);
        const currPosts = posts;

        console.log("Response Downvote: ", response);

        currPosts.forEach(
            (post: PostData) => {
                if (post.id === id) {
                    post.votes = response.data.votes;
                }
            }
        )        
        setPosts(currPosts);
    }    

    const upvoteButton = useCallback(async(id: string) => {
        console.log("Upvoting");
        await upvote(id);
        if (!upvoteSend)
            setUpvoteSend(true);
        else
            setUpvoteSend(false);

    }, []);


    const downvoteButton = useCallback(async(id: string) => {
        console.log("Downvoting");
        await downvote(id);
        if (!downvoteSend)
            setDownvoteSend(true);
        else
            setDownvoteSend(false);

    }, []);

    useEffect(() => {
        fetchUserData();
    }, [])

    const Posts = () => {
        return (
            <div>
                <form className="md:container md:mx-auto p-5 border-solid border-2
                    bg-slate-50 border-slate-300 hover:bg-slate-100">
                    <p className="text-3xl align-middle justify-between font-semibold">Create a new post</p>
                    <br />
                    <p className="text-2xl">Title: 
                        <br />
                        <input type="text"
                               key="inpTitle"
                               className="text-2xl border-black border-2 border-solid" 
                               onChange={(e) => setTitle(e.target.value)}
                               value={title}
                               autoFocus />
                    </p>
                    <br />
                    <p className="text-2xl">Body: 
                        <br />
                        <input type="text"
                               key={"inpBody"}
                               className="text-2xl mx-auto border-black border-2 border-solid"
                               onChange={e => setBody(e.target.value)}
                               value={body}
                        />
                    </p>
                    <br />
                    <button className="bg-green-700 rounded-lg p-2 text-white 
                        hover:bg-green-900"disabled={downvoteSend} >
                        Create
                    </button>
                </form>           
                <br />
                <hr />
                <br />
                {posts.map((item: PostData) => (
                    <div>
                        <div className="md:container md:mx-auto p-5 border-solid border-2
                                      bg-slate-50 border-slate-300 hover:bg-slate-100">
                            <Post id={item.id} title={item.title.trim()} body={item.body.trim()} votes={item.votes} />
                            <br />

                            <button className="bg-blue-500 rounded-lg p-2 text-white
                             hover:bg-blue-700" onClick={() => upvoteButton(item.id)}
                             disabled={upvoteSend}
                             >
                                Upvote
                            </button>
                            {' '}
                            <button className="bg-red-500 rounded-lg p-2 text-white 
                            hover:bg-red-700" onClick={() => downvoteButton(item.id)}
                            disabled={downvoteSend}
                            >
                                Downvote
                            </button>
                            {' '}
                            <button className="bg-green-700 rounded-lg p-2 text-white 
                            hover:bg-green-900" onClick={() => downvoteButton(item.id)}
                            disabled={downvoteSend}
                            >
                                Comments
                            </button>
                        </div>
                        <br />
                    </div>
                ))}
            </div>
        );
    }    

    return (
        <div>
            <Header />
            {loading ? <div>Loading data</div>: <Posts />}
        </div>
    );
}

export default Home;
