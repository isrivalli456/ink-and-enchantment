
#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from blog_writing_crew.crew import BlogWritingCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """Run the blog-writing crew for a user-provided topic."""

    topic = input("\nEnter the topic for your blog: ").strip()

    if not topic:
        print("Please enter a valid topic.")
        return

    inputs = {
        "topic": topic,
        "current_year": str(datetime.now().year),
    }

    try:
        result = BlogWritingCrew().crew().kickoff(inputs=inputs)
        print("\nBlog generation completed!")
        print("Check blog.md in your project folder for the generated blog.")
        return result
    except Exception as e:
        raise Exception(
            f"An error occurred while running the crew: {e}"
        ) from e


def train():
    """Train the crew for the requested number of iterations."""

    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year),
    }

    try:
        BlogWritingCrew().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs,
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}") from e


def replay():
    """Replay the crew from a specific task."""

    try:
        BlogWritingCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}") from e


def test():
    """Test the crew."""

    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year),
    }

    try:
        BlogWritingCrew().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs,
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}") from e


def run_with_trigger():
    """Run the crew with a trigger payload."""

    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError as e:
        raise Exception("Invalid JSON payload provided.") from e

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": str(datetime.now().year),
    }

    try:
        return BlogWritingCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(
            f"An error occurred while running the crew with trigger: {e}"
        ) from e
