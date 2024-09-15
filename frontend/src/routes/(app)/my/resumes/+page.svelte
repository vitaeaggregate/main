<script lang="ts">
  import { goto } from "$app/navigation";
  import { getResumesByMemberId } from "$lib/api/resume";
  import Button from "$lib/components/Button.svelte";
  import CommentView from "$lib/components/resume/CommentView.svelte";
  import type { Resume } from "$lib/interfaces/resume/Resume";
  import type { Comment } from "$lib/interfaces/resume/Comment";
  import { account } from "$lib/store";
  import { getCommentsByResumeId } from "$lib/api/comment";
    import { slide } from "svelte/transition";

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

  $: if ($account) loadPage();

let showComments = false;
let container;
let selectedResumeId: number | null = null;

  function toggleComments(resumeId: number) {
    selectedResumeId = resumeId === selectedResumeId ? null : resumeId;
    showComments = selectedResumeId !== null;
  }

function fadeSlide(node, options) {
  const slideTrans = slide(node, options);
  return {
    duration: options.duration,
    css: (t) => `
      ${slideTrans.css(t)}
      opacity: ${t};
    `
  };
}
</script>

{#if $account}
  <section>
    <h1>My Resumes</h1>
    <div class="h-12 w-16 rounded-xl bg-amber-600 p-3 shadow-lg mb-4 mt-4 text-center"><Button on:click={handleGoBack}>Back</Button></div>
    <div class="">
      {#if Object.keys(resumes).length}
        {#each Object.entries(resumes) as [resumeId, { resume, comments }]}
          <div class="mb-2 rounded-xl border-2 bg-white p-4">
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
            <div bind:this={container}>
              <button class="cursor-pointer"
              on:click={() => toggleComments(resumeId)}><h3
            >Comments ({comments.length})</h3></button>
          {#if resumeId === selectedResumeId}
          <div transition:fadeSlide={{ duration: 300 }} class="grid-row-4 grid gap-10">
            <CommentView value={comments} config={{ isReadyOnly: true, isResumeTitleHidden: true }}
            ></CommentView>
          </div>{/if}
          </div></div>
        {/each}
      {:else}
        <p>
          <strong>So Empty...</strong>
        </p>
      {/if}
    </div>
  </section>
{/if}