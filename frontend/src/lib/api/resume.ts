import type Resume from "$lib/interfaces/resume/Resume";

const endPoint = import.meta.env.BASE_URL;

// POST Resume Data
export const addResume = async (resume: Resume) => {
	const response = await fetch(endPoint, {
		method: "POST",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify(resume)
	});
	const json = await response.json();
	return JSON.stringify(json);
};

// DELETE Resume Data
