CREATE MIGRATION m1mbsuwh7n2ycsxtmbw3eoc4lgwli3bcorgc3fzsvoymvuaxaoyaqq
    ONTO m1uwekrn4ni4qs7ul7hfar4xemm5kkxlpswolcoyqj3xdhweomwjrq
{
  ALTER TYPE default::Movie {
      CREATE INDEX ON (.title);
  };
  ALTER TYPE default::Person {
      CREATE PROPERTY age: std::int16;
  };
};
