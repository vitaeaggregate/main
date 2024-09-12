import { PUBLIC_SERVER } from "$env/static/public";
import { fetchData } from "$lib/utils";
import { error } from "@sveltejs/kit";
import type { Comment } from "$lib/interfaces/resume/Comment";

export const getCommentsByMemberId = async (memberId: number): Promise<Comment[]> => {
	const response = await fetchData(PUBLIC_SERVER + "/members/" + memberId + "/comments/");

	if (!response.ok) throw error(response.status, response.statusText);

	const comments: Comment[] = await response.json();

	return comments;
};

export const getCommentsByResumeId = async (resumeId: number): Promise<Comment[]> => {
	const response = await fetchData(PUBLIC_SERVER + "/resumes/" + resumeId + "/comments/");

	if (!response.ok) throw error(response.status, response.statusText);

	const comments: Comment[] = await response.json();

	return comments;
};

export const createComment = async (comment: Comment): Promise<Comment> => {
	const requestInit: RequestInit = {
		method: "POST",
		body: JSON.stringify(comment)
	};

	const response = await fetchData(PUBLIC_SERVER + "/comments/", requestInit);

	const commentData: Comment = await response.json();

	return commentData;
};

export const deleteComment = async (commentId: number | string): Promise<boolean> => {
	const requestInit: RequestInit = {
		method: "DELETE"
	};
	const response = await fetchData(PUBLIC_SERVER + "/comments/" + commentId + "/", requestInit);
	if (!response.ok) throw error(response.status, response.statusText);

	return true;
};
