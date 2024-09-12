<script lang="ts">
	import type { Comment } from "$lib/interfaces/resume/Comment";
	import { writable } from "svelte/store";
	import { deleteComment, getCommentsByResumeId } from "$lib/api/comment";
	import { getResumeById } from "$lib/api/resume";
	import { account, checkAccountAndRedirect } from "$lib/store";
	import { page } from "$app/stores";
	import type { Resume } from "$lib/interfaces/resume/Resume";
	import { goto } from "$app/navigation";
	import Button from "$lib/components/Button.svelte";

	export const id = writable<number | null>(null);

	$: resumeId = Number($page.params.id);

	let resume: Resume | null = null;
	let resumesComments: { [resumeId: number]: Comment[] } = {};

	const loadPage = async () => {
		if (!$account) return;
		resume = await getResumeById(resumeId);
	};

	const handleGoBack = () => {
		goto("/community");
	};

	checkAccountAndRedirect(loadPage);
</script>

<main>
	<h1>Community</h1>
	<br />
	<Button on:click={handleGoBack}>Back</Button><br /><br />
	<div class="test-div flex justify-center">
		<div
			class="mb-16 ml-16 mr-16 flex h-screen w-4/5 flex-col overflow-y-auto border-2 border-solid border-black p-4"
		>
			{#if resume}
				{#if resume.skills === undefined}
					<br />
				{:else if resume.skills.length > 0}
					<h2 class="print:text-xl">Skills</h2>
					<ul class="text-base leading-8 print:text-sm print:leading-6">
						<ul>
							{#each resume.skills as skill}
								{#if skill.name}
									<strong>Name:</strong> {skill.name} <br />
								{/if}
								<strong>Description:</strong>
								{skill.description} <br />
								<strong>Skill Level:</strong>
								{skill.skill_level} <br /><br />
							{/each}
						</ul>
					</ul>
				{/if}
				{#if resume.professional_exps === undefined}
					<br />
				{:else if resume.professional_exps.length > 0}
					<h2 class="bg-gray-100 print:text-xl">Professional Experience</h2>
					<ul class="text-base leading-7">
						<ul>
							{#each resume.professional_exps as exp}
								<span class="float-right mr-2">
									{#if exp.start_date}
										{exp.start_date}
									{/if}
									-
									{#if exp.end_date}
										{exp.end_date} <br />
									{/if}</span
								>
								{#if exp.job_title}
									<strong class="text-xl print:text-lg">{exp.job_title}</strong><br />
								{/if} -
								{#if exp.city}<i>{exp.city}</i>{/if}{#if exp.city && exp.country},
								{/if}
								{#if exp.country}
									<i>{exp.country}</i>
								{/if}
								<br />
								{#if exp.employer}
									<strong>Employer:</strong> {exp.employer} <br />
								{/if}
								{#if exp.description}
									<strong>Description:</strong> {exp.description} <br /><br />
								{/if}
							{/each}
						</ul>
					</ul>
				{/if}
				{#if resume.awards.length > 0}
					<h2 class="bg-gray-100 print:text-xl">Awards</h2>
					<ul class="text-base leading-7">
						<ul>
							{#each resume.awards as award}
								{#if award.title}
									<strong>Title:</strong> {award.title} <br />
								{/if}
								{#if award.issuer}
									<strong>Issuer:</strong> {award.issuer} <br />
								{/if}
								{#if award.date}
									<strong>Date:</strong> {award.date} <br />
								{/if}
								{#if award.description}
									<strong>Description:</strong> {award.description} <br /><br />
								{/if}
							{/each}
						</ul>
					</ul>
				{/if}
				{#if resume.links === undefined}
					<br />
				{:else if resume.links.length > 0}
					<h2 class="bg-gray-100 print:text-xl">Links</h2>
					<ul class="text-base leading-7">
						<ul>
							{#each resume.links as link}
								<strong>Title:</strong>
								{link.title} <br />
								<strong>URL:</strong>
								{link.url} <br /><br />
							{/each}
						</ul>
					</ul>
				{/if}
				{#if resume.certificates.length > 0}
					<h2 class="bg-gray-100 print:text-xl">Certificates</h2>
					<ul class="text-base leading-7">
						<ul>
							{#each resume.certificates as certificate}
								{#if certificate.name}
									<strong>Name:</strong> {certificate.name} <br />
								{/if}
								{#if certificate.description}
									<strong>Description:</strong> {certificate.description} <br /><br />
								{/if}
							{/each}
						</ul>
					</ul>
				{/if}
				{#if resume.courses === undefined}
					<br />
				{:else if resume.courses.length > 0}
					<h2 class="bg-gray-100 print:text-xl">Courses</h2>
					<ul class="text-base leading-7">
						<ul>
							{#each resume.courses as course}
								<span class="float-right mr-2">
									{#if course.start_date}
										{course.start_date}
									{/if}
									-
									{#if course.end_date}
										{course.end_date} <br />
									{/if}</span
								>
								{#if course.degree}
									<strong class="text-xl print:text-lg">{course.degree}</strong>
								{/if} -
								{#if course.city}<i>{course.city}</i>{/if}{#if course.city && course.country},
								{/if}
								{#if course.country}
									<i>{course.country}</i>
								{/if}
								<br />
								{#if course.institution}
									<strong>Institution:</strong> {course.institution} <br />
								{/if}
								{#if course.description}
									<strong>Description:</strong> {course.description} <br /><br />
								{/if}
							{/each}
						</ul>
					</ul>
				{/if}
				{#if resume.interests === undefined}
					<br />
				{:else if resume.interests.length > 0}
					<h2 class="bg-gray-100 print:text-xl">Interests</h2>
					<ul class="text-base leading-7">
						<ul>
							{#each resume.interests as interest}
								<strong>Name:</strong>
								{interest.name} <br />
								{#if interest.description}
									<strong>Description:</strong> {interest.description} <br /><br />
								{/if}
							{/each}
						</ul>
					</ul>
				{/if}
				{#if resume.languages === undefined}
					<br />
				{:else if resume.languages.length > 0}
					<h2 class="bg-gray-100 print:text-xl">Languages</h2>
					<ul class="text-base leading-7">
						<ul>
							{#each resume.languages as lang}
								<strong>Language:</strong>
								{lang.language} <br />
								<strong>Description:</strong>
								{lang.description} <br />
								<strong>Skill Level:</strong>
								{lang.skill_level} <br /><br />
							{/each}
						</ul>
					</ul>
				{/if}
				{#if resume.projects === undefined}
					<br />
				{:else if resume.projects.length > 0}
					<h2 class="bg-gray-100 print:text-xl">Projects</h2>
					<ul class="text-base leading-7">
						<ul>
							{#each resume.projects as project}
								<strong>Title:</strong>
								{project.title} <br />
								{#if project.sub_title}
									<strong>Subtitle:</strong> {project.sub_title} <br />
								{/if}
								{#if project.start_date}
									<strong>Start Date:</strong> {project.start_date} <br />
								{/if}
								{#if project.end_date}
									<strong>End Date:</strong> {project.end_date} <br />
								{/if}
								{#if project.description}
									<strong>Description:</strong> {project.description} <br /><br />
								{/if}
							{/each}
						</ul>
					</ul>
				{/if}
				{#if resume.publications === undefined}
					<br />
				{:else if resume.publications.length > 0}
					<h2 class="bg-gray-100 print:text-xl">Publications</h2>
					<ul class="text-base leading-7">
						<ul>
							{#each resume.publications as publication}
								<strong>Title:</strong>
								{publication.title} <br />
								{#if publication.publisher}
									<strong>Publisher:</strong> {publication.publisher} <br />
								{/if}
								{#if publication.date}
									<strong>Date:</strong> {publication.date} <br />
								{/if}
								{#if publication.description}
									<strong>Description</strong> {publication.description} <br /><br />
								{/if}
							{/each}
						</ul>
					</ul>
				{/if}
			{/if}
		</div>
	</div>
	<h2>Comments</h2>
	<h3 class="mb-2">New Comment</h3>
</main>
