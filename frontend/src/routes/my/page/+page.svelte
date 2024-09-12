<script lang="ts">
	import { writable } from "svelte/store";
	import { account, checkAccountAndRedirect } from "$lib/store";
	import { getResumesByMemberId, deleteResume } from "$lib/api/resume";
	import { getCommentsByMemberId, getCommentsByResumeId } from "$lib/api/comment";
	import type { Comment } from "$lib/interfaces/resume/Comment";
	import CommentView from "$lib/components/resume/CommentView.svelte";
	import type { Resume } from "$lib/interfaces/resume/Resume";
	import Button from "$lib/components/Button.svelte";
	import { goto } from "$app/navigation";

	export const id = writable<number | null>(null);
	export const resumeId = writable<number | null>(null);

	let token: string | null = null;
	let memberComments: Comment[] = [];
	let resumes: {
		[id: string]: {
			resume: Resume;
			comments: Comment[];
		};
	} = {};

	const loadPage = async () => {
		if (!$account) return;
		token = sessionStorage.getItem("token");

		const resumesResponse = await getResumesByMemberId($account.id);

		memberComments = await getCommentsByMemberId($account.id);

		for (const resume of resumesResponse) {
			resumes[resume.id] = {
				resume,
				comments: await getCommentsByResumeId(resume.id)
			};
		}
	};

	function handleResumeDelete(resumeKey: string) {
		delete resumes[resumeKey];
		resumes = resumes;
		deleteResume(resumeKey);
	}

	checkAccountAndRedirect(loadPage);
</script>

{#if $account}
	<section class="">
		<h1>Dashboard</h1>
		<div class="">
			<div>
				<h2>User Info</h2>
				<div class="mb-2 border-2 bg-slate-200 p-2">
					<p><strong>Email: </strong>{$account.email}</p>
				</div>
			</div>
			<div>
				<h2>Resumes</h2>
				<div class="mb-2 border-2 bg-slate-200 p-2">
					<div>
						<Button on:click={() => goto("/my/resumes/new")}>Add Resume</Button>
						<Button on:click={() => goto("/my/resumes")}>Full list</Button>
					</div>
					<div class="flex flex-col divide-y divide-black">
						{#if Object.keys(resumes).length}
							{#each Object.entries(resumes) as [resumeId, { resume, comments }] (resumeId)}
								<div class="p-4">
									<a href={`/my/resumes/${resumeId}`}>
										<span class="text-xl hover:font-medium">
											{resume.title}
										</span>
									</a>
									<p><strong>Shared:</strong> {resume.is_shareable ? "Yes" : "No"}</p>
									<h3>Comments</h3>
									<CommentView
										bind:value={comments}
										config={{ isReadyOnly: true, isResumeTitleHidden: true }}
									></CommentView>
									<Button on:click={() => handleResumeDelete(resumeId)}>Delete Resume</Button>
								</div>
							{/each}
						{:else}
							<p><strong>No Resumes</strong></p>
						{/if}
					</div>
				</div>
			</div>
			<div>
				<h2>Community</h2>
				<div class="mb-2 border-2 bg-slate-200 p-2">
					<h3>Your Comments</h3>
					<CommentView
						bind:value={memberComments}
						config={{ isReadyOnly: true, isResumeTitleHidden: false }}
					></CommentView>
				</div>
			</div>
		</div>
	</section>
{/if}
