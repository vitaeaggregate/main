<script lang="ts">
  export let print = false;
  // manual edit in style tag
  const appId = "AppPdf_id";

  // 		storing display computed
  let displays: never[] = [];

  const selectorNotApp = `:not(#${appId}):not(#${appId} *):not(script):not(link)`;

  // temporary element store when find element
  let stackElements: any[] = [];
  const findElementIsNotAppPdf = (
    el,
    selector: string,
    callback: {
      (el: Element, i: string | number): void;
      (el: any, i: any): void;
      (arg0: any, arg1: number): void;
    },
    _props = { i: 0 } // need reference object
  ) => {
    el.querySelectorAll(selector).forEach((el: { querySelector: (arg0: string) => any }) => {
      if (el.querySelector("#" + appId)) {
        findElementIsNotAppPdf(el, selectorNotApp, callback, _props);
      } else {
        if (!stackElements.includes(el)) {
          callback(el, _props.i++);
          stackElements.push(el);
        }
      }
    });
  };

  $: if (print) {
    // Set all display element except AppPdf to none
    findElementIsNotAppPdf(
      document.body,
      `body > ${selectorNotApp}`,
      (el: Element, i: string | number) => {
        displays[i] = window.getComputedStyle(el).display;
        el.style.display = "none";
      }
    );
    // set to empty because is done
    stackElements = [];

    // 		print now
    window.print();

    // show them back
    findElementIsNotAppPdf(document.body, `body > ${selectorNotApp}`, (el, i) => {
      el.style.display = displays[i];
    });
    // set to empty because is done
    stackElements = [];

    // reset display
    displays = [];
    print = false;
  }
</script>

<span id={appId}>
  <slot />
</span>

<style>
  @media print {
    #AppPdf_id {
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }
    :global(table, img, svg, p) {
      page-break-inside: auto;
    }
  }
</style>
