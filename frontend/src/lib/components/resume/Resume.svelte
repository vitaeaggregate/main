<script lang="ts">
  import PersonalInfo from "$lib/components/resume/PersonalInfo.svelte";
  import Skill from "$lib/components/resume/Skill.svelte";
  import Award from "$lib/components/resume/Award.svelte";
  import Certificate from "$lib/components/resume/Certificate.svelte";
  import Course from "$lib/components/resume/Course.svelte";
  import Education from "$lib/components/resume/Education.svelte";
  import Language from "$lib/components/resume/Language.svelte";
  import Interest from "$lib/components/resume/Interest.svelte";
  import Link from "$lib/components/resume/Link.svelte";
  import ProfessionalExp from "$lib/components/resume/ProfessionalExp.svelte";
  import Project from "$lib/components/resume/Project.svelte";
  import Publication from "$lib/components/resume/Publication.svelte";
  import Reference from "$lib/components/resume/Reference.svelte";
  import InputText from "$lib/components/InputText.svelte";
  import InputCheckBox from "$lib/components/InputCheckBox.svelte";
  import type { BaseResume } from "$lib/interfaces/resume/Resume";
  import { type ComponentType } from "svelte";
  import Button from "$lib/components/Button.svelte";
  import Modal from "../Modal.svelte";
  import ComponentView from "./ComponentView.svelte";

  export const id: number | null = null;
  export let value: BaseResume;

  type ArrayKeys<Type> = {
    [key in keyof Type]: Type[key] extends Array<any> ? key : never;
  }[keyof Type];

  type ComponentMapping = {
    key: ArrayKeys<BaseResume>;
    label: string;
    component: ComponentType;
    componentValue: { id?: string | number };
  };

  let isModalHidden: boolean = true;
  let currentSectionMap: ComponentMapping | null = null;
  let backModalClick: (() => void) | null = null;

  const componentMap: { [text: string]: ComponentMapping } = {
    ...mapComponent("Professional Experience", "professional_exps", ProfessionalExp),
    ...mapComponent("Link", "links", Link),
    ...mapComponent("Skill", "skills", Skill),
    ...mapComponent("Award", "awards", Award),
    ...mapComponent("Certificate", "certificates", Certificate),
    ...mapComponent("Course", "courses", Course),
    ...mapComponent("Education", "educations", Education),
    ...mapComponent("Interest", "interests", Interest),
    ...mapComponent("Language", "languages", Language),
    ...mapComponent("Project", "projects", Project),
    ...mapComponent("Publication", "publications", Publication),
    ...mapComponent("Reference", "references", Reference)
  };

  function mapComponent(
    text: string,
    key: ArrayKeys<BaseResume>,
    component: ComponentType
  ): { [text: string]: ComponentMapping } {
    return {
      [text]: {
        key,
        label: text,
        component,
        componentValue: {}
      }
    };
  }

  const addSection = (section: ComponentMapping) => {
    if (!section || !section.key) return;
    currentSectionMap = section;
    value[section.key] = [...value[section.key], {}];
  };

  const addCurrentSection = () => {
    if (!currentSectionMap || !currentSectionMap.key) return;
    // Add the next
    value[currentSectionMap.key] = [...value[currentSectionMap.key], {}];
    currentSectionMap.componentValue = {};
  };

  const closeModalClick = (event?: Event) => {
    if (event instanceof KeyboardEvent && event.key !== "Enter") return;
    currentSectionMap = null;
    isModalHidden = true;
  };

  const cancelCurrentSection = () => {
    if (!currentSectionMap || !currentSectionMap.key) return;
    // Remove the last addition
    removeLast();
    resetComponent();
    closeModalClick();
  };

  const removeLast = () => {
    if (currentSectionMap && currentSectionMap.key)
      value[currentSectionMap.key] = [
        ...value[currentSectionMap.key].splice(0, value[currentSectionMap.key].length - 1)
      ];
  };

  const resetComponent = () => {
    if (!currentSectionMap) return;
    currentSectionMap.componentValue = {};
    currentSectionMap = null;
  };

  $: {
    if (currentSectionMap)
      backModalClick = () => {
        if (currentSectionMap && Object.keys(currentSectionMap.componentValue).length === 1)
          removeLast();
        resetComponent();
      };
    else backModalClick = null;
  }

  $: {
    if (currentSectionMap && currentSectionMap.key && currentSectionMap.componentValue) {
      // value[currentSection.key] --> value.skills, value.links
      if (value[currentSectionMap.key].length) {
        value[currentSectionMap.key] = value[currentSectionMap.key].map((section) => {
          if (
            currentSectionMap &&
            currentSectionMap.componentValue &&
            currentSectionMap.componentValue.id == section.id
          )
            return currentSectionMap.componentValue;
          else return section;
        });
      }
    }
  }
</script>

<section>
  {#if !isModalHidden}
    <Modal closeClick={closeModalClick} backClick={backModalClick}>
      <div>
        <div class="flex justify-center">
          <h2>Add Section</h2>
        </div>
        {#if !currentSectionMap}
          <div class="flex flex-wrap justify-center gap-5">
            {#each Object.entries(componentMap) as [text, map], index (index)}
              <Button on:click={() => addSection(map)}>{text}</Button>
            {/each}
          </div>
        {:else}
          <div class="flex flex-col gap-4">
            <ComponentView
              bind:component={currentSectionMap.component}
              bind:value={currentSectionMap.componentValue}
              config={{ unitLabel: currentSectionMap.label }}
            ></ComponentView>
            <div class="flex justify-between">
              <Button on:click={addCurrentSection}>Add</Button>
              <Button on:click={cancelCurrentSection}>Cancel</Button>
            </div>
          </div>
        {/if}
      </div>
    </Modal>
  {/if}
  <div class="flex flex-col gap-5">
    <div class="flex flex-col gap-2">
      <InputText label="Resume Name" required={true} bind:value={value.title} />
      <InputCheckBox label="Share" bind:value={value.is_shareable}></InputCheckBox>
    </div>
    <PersonalInfo bind:value={value.personal_info}></PersonalInfo>
    <div class="flex flex-col items-start justify-center gap-5">
      {#each Object.entries(componentMap) as [text, map], index (index)}
        {#if map.key}
          <ComponentView
            bind:value={value[map.key]}
            component={map.component}
            config={{ readOnly: true, unitLabel: text }}
          ></ComponentView>
        {/if}
      {/each}
    </div>
  </div>
  <div class="fixed bottom-0 right-0 m-9 border-2 bg-slate-200 p-2">
    <Button on:click={() => (isModalHidden = false)}>Add Section</Button>
  </div>
</section>
