import { PUBLIC_SERVER } from "$env/static/public";
import type Resume from "$lib/interfaces/resume/Resume";
import { fetchData } from "$lib/utils";
import { error } from "@sveltejs/kit";

export const getResumesByMemberId = async (memberId: number): Promise<Resume[] | null> => {
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

	return resumes.length ? resumes : null;
};

// POST Resume Data
export const addResume = async (memberId: number, resume: Resume): Promise<Resume> => {
	const requestInit: RequestInit = {
		method: "POST",
		body: JSON.stringify(resume)
	};
	const response = await fetchData(
		PUBLIC_SERVER + "/members/" + memberId + "/resumes/",
		requestInit
	);
	if (!response.ok) {
		throw error(response.status, response.statusText);
	}

	const resumeData: Resume = await response.json();

	return resumeData;
};

// DELETE Resume Data
