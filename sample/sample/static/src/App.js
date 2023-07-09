import React, { useEffect, useState } from "react";

const Quiz = () => {
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    fetch("/api/questions/")
      .then((response) => response.json())
      .then((data) => setQuestions(data))
      .catch((error) => console.error(error));
  }, []);

  return (
    <div>
      <h1>Quiz</h1>
      {questions.map((question) => (
        <div key={question.id}>
          <h3>{question.text}</h3>
          {question.choices.map((choice) => (
            <label key={choice.id}>
              <input
                type="radio"
                name={`question-${question.id}`}
                value={choice.id}
              />
              {choice.text}
            </label>
          ))}
        </div>
      ))}
    </div>
  );
};

export default Quiz;
