# researcher.py
import typer
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from duckduckgo_search import DDGS

# Initialize Rich Console for beautiful printing
console = Console()

app = typer.Typer()

@app.command()
def search(
    query: str = typer.Argument(..., help="The search query."),
    num_results: int = typer.Option(5, "--num", "-n", help="Number of search results to display.")
):
    """
    Performs a web search and displays the top results.
    """
    console.print(f"[bold blue]🔎 Searching for: '{query}'...[/bold blue]")

    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=num_results)]

        if not results:
            console.print("[bold red]❌ No results found.[/bold red]")
            raise typer.Exit()

        console.print(f"\n[bold green]✅ Here are the top {len(results)} results:[/bold green]\n")

        for i, result in enumerate(results):
            # Create a panel for each result
            panel_content = f"""
**Title**: {result['title']}
**Link**: [link={result['href']}]{result['href']}[/link]

---
{result['body']}
            """
            console.print(
                Panel(
                    Markdown(panel_content),
                    title=f"[bold cyan]Result {i+1}[/bold cyan]",
                    border_style="cyan",
                    expand=True
                )
            )

    except Exception as e:
        console.print(f"[bold red]An error occurred: {e}[/bold red]")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
