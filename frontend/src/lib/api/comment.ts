import { PUBLIC_SERVER } from "$env/static/public";
import { fetchData } from "$lib/utils";
import { error } from "@sveltejs/kit";
import type Comment from "$lib/interfaces/resume/Comment";

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
		PUBLIC_SERVER + "/members/" + memberId + "/resumes/" + resumeId + "/comments"
	);

	if (!response.ok) throw error(response.status, response.statusText);

	const comments: Comment[] = await response.json();

	return comments;
};
