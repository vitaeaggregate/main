<script lang="ts">
  import type { Comment } from "$lib/interfaces/resume/Comment";
  import { createComment, deleteComment, getCommentsByResumeId } from "$lib/api/comment";
  import { getResumeById } from "$lib/api/resume";
  import { account } from "$lib/store";
  import { page } from "$app/stores";
  import type { Resume } from "$lib/interfaces/resume/Resume";
  import { goto } from "$app/navigation";
  import Button from "$lib/components/Button.svelte";
  import CommentView from "$lib/components/resume/CommentView.svelte";
  import ResumePreview from "$lib/components/resume/ResumePreview.svelte";

  let resume: Resume | null = null;
  let resumeComments: Comment[] = [];
  let newComment: Comment = {
    description: ""
  };

  let resumeElement: HTMLElement | null = null;
  let previewContainer: HTMLDivElement | null = null;
  let previewContainerWidth: number;
  let resumeElementSize: {
    height: number;
    width: number;
  } = {
    height: 0,
    width: 0
  };

  const loadPage = async () => {
    resume = await getResumeById($page.params.id);
    resumeComments = await getCommentsByResumeId($page.params.id);
  };

  const handleGoBack = () => goto("/community");

  const handleNewComment = async () => {
    if (!$account) return;
    newComment.member = $account.id;
    newComment.header = $page.params.id;
    const comment = await createComment(newComment);
    resumeComments.push(comment);
    resumeComments = resumeComments;
    newComment = {};
  };

  $: {
    if (previewContainer && previewContainerWidth && resumeElement && resumeElementSize) {
      const scale = previewContainerWidth / resumeElementSize.width;
      resumeElement.style.transform = `scale(${scale})`;
      const currentHeight = Math.round(resumeElementSize.height * scale);
      previewContainer.style.height = currentHeight + "px";
    }
  }

  $: if ($page.params.id && $account) loadPage();
</script>

{#if $account}
  <section>
    <h1>Community</h1>
    <Button on:click={handleGoBack}>Back</Button><br /><br />
    {#if resume}
      <div class="rounded-lg bg-slate-100 p-5 shadow-lg">
        <div bind:this={previewContainer} bind:clientWidth={previewContainerWidth}>
          <ResumePreview bind:resume bind:resumeElement bind:resumeElementSize></ResumePreview>
        </div>
      </div>
    {/if}
    <h2>Comments</h2>
    <CommentView
      bind:value={resumeComments}
      config={{ isReadyOnly: true, isResumeTitleHidden: true }}
    ></CommentView>
    <h2 class="mb-2">New Comment</h2>
    <CommentView bind:value={newComment} config={{ isReadyOnly: false, isResumeTitleHidden: true }}
    ></CommentView>
    <Button on:click={handleNewComment}>Send</Button>
  </section>
{/if}
