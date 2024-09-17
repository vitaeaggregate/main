<script lang="ts">
  import { page } from "$app/stores";
  import { deleteResume, getResumeById, updateResume } from "$lib/api/resume";
  import { account, addToast } from "$lib/store";
  import type { Resume } from "$lib/interfaces/resume/Resume";
  import { goto } from "$app/navigation";
  import Button from "$lib/components/Button.svelte";
  import ResumePreview from "$lib/components/resume/ResumePreview.svelte";
  import ResumeComponent from "$lib/components/resume/Resume.svelte";
  import Toasts from "$lib/components/Toasts.svelte";
  import DeleteIcon from "$lib/icons/DeleteIcon.svelte";
  import DownloadIcon from "$lib/icons/DownloadIcon.svelte";

  let resume: Resume | null = null;
  let originalResume: string | null = null;
  let isModified = false;
  let isDownloaded: Promise<Boolean>;
  let isDownloadStarted = false;

  let previewContainer: HTMLDivElement | null = null;
  let previewContainerWidth: number;
  let resumeElement: HTMLElement | null = null;
  let resumeElementSize: {
    height: number;
    width: number;
  } = {
    height: 0,
    width: 0
  };

  // Toasts config
  let message = "One or more fields are incorrect!";
  let type = "error";
  let dismissible = true;
  let timeout = 3000;
  // ---------------

  const loadResume = async () => {
    resume = await getResumeById($page.params.id);
    originalResume = JSON.stringify(resume);
  };

  const handleSaveClick = async () => {
    try {
      if (!$account || !resume) return;
      const updatedResume: Resume = await updateResume(resume);
      resume = updatedResume;
      originalResume = JSON.stringify(resume);
    } catch {
      addToast({
        message,
        type,
        dismissible,
        timeout
      });
    }
  };

  const handleCancelClick = () => {
    if (!originalResume) return;
    resume = JSON.parse(originalResume);
  };

  const handleResumeDelete = () => {
    if (!resume) return;
    deleteResume(resume.id);
    goto("/my/page");
  };

  const handleDownloadClick = () => {
    isDownloaded = downloadPdf();
  };

  const downloadPdf = async () => {
    if (!resume || !resumeElement) throw console.error("Resume not loaded.");

    isDownloadStarted = true;

    const body = resumeElement.innerHTML;

    const response = await fetch("./resumes", {
      method: "POST",
      headers: {
        "Content-Type": "applications/json"
      },
      body: JSON.stringify({ body })
    });

    if (!response.ok) throw console.error("Fetch error");

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const invisibleLink = document.createElement("a");
    invisibleLink.href = url;
    invisibleLink.download = "resume.pdf";
    invisibleLink.click();
    URL.revokeObjectURL(url);

    isDownloadStarted = false;

    return true;
  };

  $: if ($account && $page.params.id) loadResume();

  $: isModified = originalResume !== JSON.stringify(resume);

  $: {
    if (previewContainer && previewContainerWidth && resumeElement && resumeElementSize) {
      const scale = previewContainerWidth / resumeElementSize.width;
      resumeElement.style.transform = `scale(${scale})`;
      const currentHeight = Math.round(resumeElementSize.height * scale);
      previewContainer.style.height = currentHeight + "px";
    }
  }
</script>

{#if $account && $page.params.id && resume}
  <Toasts />
  <section>
    <div class="mb-4 flex gap-3">
      <Button on:click={handleResumeDelete} style="labeled-icon">
        <span class="flex flex-col gap-6">
          <DeleteIcon />
          Delete
        </span>
      </Button>
      <Button on:click={handleDownloadClick} style="labeled-icon" disabled={isDownloadStarted}>
        <span class="flex flex-col gap-6">
          <DownloadIcon />
          {#if !isDownloadStarted}
            Download
          {:else}
            {#await isDownloaded}
              Downloading...
            {:catch}
              Error downloading the file.
            {/await}
          {/if}
        </span>
      </Button>
    </div>
    <div class="grid grid-cols-1 gap-10 overflow-hidden">
      <ResumeComponent bind:value={resume}></ResumeComponent>
      {#if isModified}
        <div
          class="fixed bottom-0 right-0 z-10 flex w-full justify-between gap-5 border-2 bg-slate-100 p-2"
        >
          <Button on:click={handleSaveClick} style="add">Save</Button>
          <Button on:click={handleCancelClick} style="cancel">Cancel</Button>
        </div>
      {/if}
      <div class="rounded-lg bg-slate-100 p-5 shadow-lg">
        <div bind:this={previewContainer} bind:clientWidth={previewContainerWidth}>
          <ResumePreview bind:resume bind:resumeElement bind:resumeElementSize></ResumePreview>
        </div>
      </div>
    </div>
  </section>
{/if}
