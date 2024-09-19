interface ButtonProps {
    text: string;
    onClick?: () => void;
  }
  
  export const Button: React.FC<ButtonProps> = ({ text, onClick }) => (
    <button
      onClick={onClick}
      className="bg-indigo-500 text-white py-2 px-4 rounded-md hover:bg-indigo-600"
    >
      {text}
    </button>
  );
  