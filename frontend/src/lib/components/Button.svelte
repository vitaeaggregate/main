<script context="module" lang="ts">
  export type Style = "default" | "submit";
</script>

<script lang="ts">
  export let style: Style = "default";
  let classes: string = "size-fit ";

  switch (style) {
    case "default": {
      break;
    }
    case "submit": {
      classes +=
        "border-2 bg-white pl-3 pr-3 pt-1 pb-1 m-auto hover:bg-lime hover:text-white hover:ease-in duration-200 rounded-md";
      break;
    }
  }
</script>

<button type="button" on:click class={classes}>
  <slot></slot>
</button>
