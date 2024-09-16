<script context="module" lang="ts">
  export type Style =
    | "default"
    | "submit"
    | "full-width"
    | "add"
    | "cancel"
    | "sections"
    | "delete"
    | "delete-md"
    | "labeled-icon";
</script>

<script lang="ts">
  export let style: Style = "default";
  let classes: string;

  switch (style) {
    case "default": {
      classes = "size-fit";
      break;
    }
    case "submit": {
      classes =
        "size-fit border-2 bg-lime pl-4 pr-4 pt-2 pb-2 m-auto rounded-xl shadow-lg hover:bg-green hover:ease-in duration-200";
      break;
    }
    case "full-width": {
      classes = "w-full";
      break;
    }
    case "add": {
      classes =
        "size-fit h-max w-max rounded-xl bg-lime p-3 shadow-lg text-center bg-opacity-80 hover:bg-green hover:ease-in duration-200";
      break;
    }
    case "cancel": {
      classes = "size-fit h-max w-max rounded-xl bg-grayish p-3 shadow-lg text-center hover:bg-red hover:ease-in duration-200";
      break;
    }
    case "sections": {
      classes = "size-fit bg-white border-2 rounded-lg p-3 hover:bg-green hover:ease-in duration-200";
      break;
    }
    case "delete": {
      classes = "size-fit flex h-max w-max rounded-xl bg-grayish p-3 shadow-lg hover:bg-red hover:ease-in duration-200";
      break;
    }
    case "delete-md": {
      classes = "flex h-max rounded-xl bg-grayish p-3 shadow-lg justify-center w-20 hover:bg-red hover:ease-in duration-200";
      break;
    }
    case "labeled-icon": {
      classes = "flex gap-3 h-max w-44 h-20 rounded-xl bg-white p-3 shadow-lg justify-left items-center hover:bg-green hover:ease-in duration-200";
    }
  }
</script>

<button type="button" on:click class={classes}>
  <slot></slot>
</button>
