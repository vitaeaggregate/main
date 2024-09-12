import { PUBLIC_SERVER } from "$env/static/public";
import type { BaseResume, Resume } from "$lib/interfaces/resume/Resume";
import { fetchData } from "$lib/utils";
import { error } from "@sveltejs/kit";

export const getResumesByMemberId = async (memberId: number): Promise<Resume[]> => {
	const response = await fetchData(PUBLIC_SERVER + "/members/" + memberId + "/resumes");

	if (!response.ok) throw error(response.status, response.statusText);

	const resumes: Resume[] = await response.json();
	return resumes;
};

// TODO Remove this
export const getResumesByResumeId = async (resumeId: number): Promise<Resume[]> => {
	const response = await fetchData(PUBLIC_SERVER + "/resumes/" + resumeId + "/");

	if (!response.ok) throw error(response.status, response.statusText);

	const resumes: Resume[] = await response.json();

	return resumes;
};

export const getResumeByMemberIdByResumeId = async (
	memberId: number,
	resumeId: number
): Promise<Resume> => {
	const response = await fetchData(PUBLIC_SERVER + "/members/" + memberId + "/resumes/" + resumeId);

	if (!response.ok) throw error(response.status, response.statusText);

	const resume: Resume = await response.json();

	return resume;
};

export const getAllResumes = async (): Promise<Resume[]> => {
	const response = await fetchData(PUBLIC_SERVER + "/resumes");

	if (!response.ok) throw error(response.status, response.statusText);

	const resumes: Resume[] = await response.json();

	return resumes;
};

export const createResume = async (resume: BaseResume): Promise<Resume> => {
	const requestInit: RequestInit = {
		method: "POST",
		body: JSON.stringify(resume)
	};

	const response = await fetchData(
		PUBLIC_SERVER + "/resumes/",
		requestInit
	);

	const resumeData: Resume = await response.json();

	return resumeData;
};

export const updateResume = async (resume: Resume): Promise<Resume> => {
	const requestInit: RequestInit = {
		method: "PATCH",
		body: JSON.stringify(resume)
	};
	
	const response = await fetchData(
		PUBLIC_SERVER + "/resumes/" + resume.id + "/",
		requestInit
	);
	if (!response.ok) throw error(response.status, response.statusText);

	const resumeUpdated: Resume = await response.json();

	return resumeUpdated;
};

export const deleteResume = async (resumeId: number): Promise<boolean> => {
	const requestInit: RequestInit = {
		method: "DELETE"
	};
	const response = await fetchData(
		PUBLIC_SERVER + "/resumes/" + resumeId + "/",
		requestInit
	);
	if (!response.ok) throw error(response.status, response.statusText);

	return true;
};
