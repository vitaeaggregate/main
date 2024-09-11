import { PUBLIC_SERVER } from "$env/static/public";
import { fetchData } from "$lib/utils";
import { error } from "@sveltejs/kit";
import type { BaseComment, Comment } from "$lib/interfaces/resume/Comment";

export const getCommentsByMemberId = async (memberId: number): Promise<Comment[]> => {
	const response = await fetchData(PUBLIC_SERVER + "/members/" + memberId + "/comments/");

	if (!response.ok) throw error(response.status, response.statusText);

	const comments: Comment[] = await response.json();

	return comments;
};

export const getCommentsByMemberIdByResumeId = async (
	memberId: number,
	resumeId: number
): Promise<Comment[]> => {
	const response = await fetchData(
		PUBLIC_SERVER + "/members/" + memberId + "/resumes/" + resumeId + "/comments/"
	);

	if (!response.ok) throw error(response.status, response.statusText);

	const comments: Comment[] = await response.json();

	return comments;
};

// POST Comment
export const createComment = async (
	memberId: number,
	resumeId: number,
	comment: BaseComment
): Promise<Comment> => {
	const requestInit: RequestInit = {
		method: "POST",
		body: JSON.stringify(comment)
	};

	const response = await fetchData(
		PUBLIC_SERVER + "/members/" + memberId + "/resumes/" + resumeId + "/comments/",
		requestInit
	);

	if (!response.ok) {
		throw error(response.status, response.statusText);
	}

	const resumeData: Comment = await response.json();

	return resumeData;
};

// DELETE Comment
export const deleteComment = async (
	memberId: number,
	resumeId: number,
	commentId: number
): Promise<boolean> => {
	const requestInit: RequestInit = {
		method: "DELETE"
	};
	const response = await fetchData(
		PUBLIC_SERVER +
			"/members/" +
			memberId +
			"/resumes/" +
			resumeId +
			"/comments/" +
			commentId +
			"/",
		requestInit
	);
	if (!response.ok) throw error(response.status, response.statusText);

	return true;
};
