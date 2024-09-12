<script lang="ts">
	import { goto } from "$app/navigation";
	import { getResumesByMemberId } from "$lib/api/resume";
	import Button from "$lib/components/Button.svelte";
	import CommentView from "$lib/components/resume/CommentView.svelte";
	import type { Resume } from "$lib/interfaces/resume/Resume";
	import type { Comment } from "$lib/interfaces/resume/Comment";
	import { account, checkAccountAndRedirect } from "$lib/store";
	import { getCommentsByResumeId } from "$lib/api/comment";

	let resumes: {
		[id: number]: {
			resume: Resume;
			comments: Comment[];
		};
	} = {};

	const loadPage = async () => {
		if (!$account) return;
		const results = await getResumesByMemberId($account.id);

		for (const resume of results) {
			resumes[resume.id] = {
				resume,
				comments: await getCommentsByResumeId(resume.id)
			};
		}
	};

	const handleGoBack = () => goto("/my/page");

	checkAccountAndRedirect();

	$: if ($account) loadPage();
</script>

{#if $account}
	<section>
		<h1>My Resumes</h1>
		<Button on:click={handleGoBack}>Back</Button>
		<div>
			{#if Object.keys(resumes).length}
				{#each Object.entries(resumes) as [resumeId, { resume, comments }]}
					<div>
						<h2>
							<a href={`/my/resumes/${resumeId}`}>
								{resume.title}
							</a>
						</h2>
						<p>
							<strong>Resume Id:</strong>
							{resumeId}
						</p>
						<p>
							<strong>Created at:</strong>
							{resume.created_at && new Date(resume.created_at).toLocaleDateString()}
						</p>
						<p>
							<strong>Updated at:</strong>
							{resume.updated_at && new Date(resume.updated_at).toLocaleDateString()}
						</p>
						<h3>Comments:</h3>
						<CommentView value={comments} config={{ isReadyOnly: true, isResumeTitleHidden: true }}
						></CommentView>
					</div>
				{/each}
			{:else}
				<p>
					<strong>So Empty...</strong>
				</p>
			{/if}
		</div>
	</section>
{/if}
