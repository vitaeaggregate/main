import { PUBLIC_SERVER } from "$env/static/public";
import type { BaseResume, Resume } from "$lib/interfaces/resume/Resume";
import { fetchData } from "$lib/utils";
import { error } from "@sveltejs/kit";

export const getResumesByMemberId = async (memberId: number): Promise<Resume[]> => {
	const requestInit: RequestInit = {
		method: "GET"
	};

	const response = await fetchData(
		PUBLIC_SERVER + "/members/" + memberId + "/resumes",
		requestInit
	);

	if (!response.ok) {
		throw error(response.status, response.statusText);
	}

	const resumes: Resume[] = await response.json();

	return resumes;
};

export const createResume = async (memberId: number, resume: BaseResume): Promise<Resume> => {
	const requestInit: RequestInit = {
		method: "POST",
		body: JSON.stringify(resume)
	};

	const response = await fetchData(
		PUBLIC_SERVER + "/members/" + memberId + "/resumes/",
		requestInit
	);

	const resumeData: Resume = await response.json();

	return resumeData;
};

export const deleteResume = async (memberID: number, resume: number): Promise<boolean> => {
	const requestInit: RequestInit = {
		method: "DELETE"
	};
	const response = await fetchData(
		PUBLIC_SERVER + "/members/" + memberID + "/resumes/" + resume + "/",
		requestInit
	);
	if (!response.ok) {
		throw error(response.status, response.statusText);
	}
	return true;
};
